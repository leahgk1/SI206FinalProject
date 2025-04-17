import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

def analyze_attractions_by_city(top_n=10):
    # Connect to the database
    conn = sqlite3.connect('travel_project.db')
    
    # Query 1: Get average rating and count of attractions by city
    query_avg_rating = """
    SELECT c.name AS city, 
           COUNT(a.id) AS attraction_count, 
           AVG(a.rating) AS avg_rating
    FROM attractions a
    JOIN cities c ON a.city_id = c.id
    GROUP BY c.name
    ORDER BY avg_rating DESC
    """
    
    # Query 2: Get attractions by category for each city
    query_category = """
    SELECT c.name AS city, 
           a.category, 
           COUNT(a.id) AS count,
           AVG(a.rating) AS avg_rating
    FROM attractions a
    JOIN cities c ON a.city_id = c.id
    GROUP BY c.name, a.category
    ORDER BY c.name, count DESC
    """
    
    # Load data into pandas DataFrames
    cities_df = pd.read_sql_query(query_avg_rating, conn)
    attractions_by_category_df = pd.read_sql_query(query_category, conn)
    
    # Filter for top N cities
    top_cities = cities_df.head(top_n)['city'].tolist()
    attractions_by_category_df = attractions_by_category_df[
        attractions_by_category_df['city'].isin(top_cities)
    ]
    
    # Close the connection
    conn.close()
    
    return cities_df, attractions_by_category_df

def generate_visualizations(cities_df, attractions_by_category_df, output_dir='visualizations'):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Set Seaborn style
    sns.set(style="whitegrid")
    
    # Visualization 1: Bar chart of average ratings by city
    plt.figure(figsize=(12, 8))
    chart = sns.barplot(x='city', y='avg_rating', data=cities_df.head(10), palette='viridis')
    chart.set_xticklabels(chart.get_xticklabels(), rotation=45, horizontalalignment='right')
    plt.title('Average Attraction Ratings by City', fontsize=16)
    plt.xlabel('City', fontsize=14)
    plt.ylabel('Average Rating (out of 5)', fontsize=14)
    plt.tight_layout()
    
    # Save the figure
    vis1_path = os.path.join(output_dir, 'average_ratings_by_city.png')
    plt.savefig(vis1_path)
    plt.close()
    
    # Visualization 2: Scatter plot of rating vs. count with size representing count
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(
        cities_df['avg_rating'], 
        cities_df['attraction_count'],
        s=cities_df['attraction_count'] * 5,  # Size proportional to count
        alpha=0.6,
        c=cities_df['avg_rating'],  # Color by rating
        cmap='viridis'
    )
    
    # Add city labels to points
    for i, row in cities_df.iterrows():
        plt.annotate(
            row['city'],
            (row['avg_rating'], row['attraction_count']),
            xytext=(5, 5),
            textcoords='offset points'
        )
    
    plt.colorbar(scatter, label='Average Rating')
    plt.title('Attraction Count vs. Average Rating by City', fontsize=16)
    plt.xlabel('Average Rating (out of 5)', fontsize=14)
    plt.ylabel('Number of Attractions', fontsize=14)
    plt.tight_layout()
    
    # Save the figure
    vis2_path = os.path.join(output_dir, 'count_vs_rating_scatter.png')
    plt.savefig(vis2_path)
    plt.close()
    
    # Visualization 3 (additional): Heatmap of category distribution
    # Pivot the data to create a matrix of cities and categories
    category_pivot = attractions_by_category_df.pivot_table(
        index='city', 
        columns='category', 
        values='count',
        fill_value=0
    )
    
    plt.figure(figsize=(14, 10))
    sns.heatmap(category_pivot, annot=True, cmap='YlGnBu', fmt='g')
    plt.title('Distribution of Attraction Categories by City', fontsize=16)
    plt.tight_layout()
    
    # Save the figure
    vis3_path = os.path.join(output_dir, 'category_distribution_heatmap.png')
    plt.savefig(vis3_path)
    plt.close()
    
    return [vis1_path, vis2_path, vis3_path]

def write_analysis_to_file(cities_df, attractions_by_category_df, output_file='attraction_analysis.txt'):
    with open(output_file, 'w') as f:
        f.write("ATTRACTION ANALYSIS RESULTS\n")
        f.write("==========================\n\n")
        
        f.write("AVERAGE RATINGS BY CITY\n")
        f.write("-----------------------\n")
        for index, row in cities_df.iterrows():
            f.write(f"{row['city']}: {row['avg_rating']:.2f} stars (from {row['attraction_count']} attractions)\n")
        
        f.write("\n\nATTRACTION CATEGORIES BY CITY\n")
        f.write("----------------------------\n")
        current_city = None
        for index, row in attractions_by_category_df.iterrows():
            if current_city != row['city']:
                current_city = row['city']
                f.write(f"\n{current_city}:\n")
            f.write(f"  {row['category']}: {row['count']} attractions (avg rating: {row['avg_rating']:.2f})\n")
    
    print(f"Analysis written to {output_file}")
    return output_file

def main():
    print("Analyzing attractions data...")
    cities_df, attractions_by_category_df = analyze_attractions_by_city()
    
    print("Generating visualizations...")
    vis_paths = generate_visualizations(cities_df, attractions_by_category_df)
    print(f"Visualizations saved to: {', '.join(vis_paths)}")
    
    print("Writing analysis to file...")
    analysis_path = write_analysis_to_file(cities_df, attractions_by_category_df)
    
    print("\nAnalysis complete!")
    print(f"- Text analysis: {analysis_path}")
    print(f"- Visualizations: {', '.join(vis_paths)}")

if __name__ == "__main__":
    main() 