import argparse
from datetime import datetime
from utils.model import get_valid_catoricals

# Custom function to parse date strings
def valid_date(s):
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid date: '{s}'. Format should be YYYY-MM-DD.")


def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool")
    
    parser.add_argument("name", type=str, help="Your Project Name")
    parser.add_argument("category", type=str, help="Your Project Category")
    parser.add_argument("subcategory", type=str, help="Your Project Sub-Category")
    parser.add_argument("country", type=str, help="Your Country")

    parser.add_argument("date_launched", type=valid_date, help="Your Project Launch Date")
    parser.add_argument("date_deadline", type=valid_date, help="Your Project Deadline Date")
    parser.add_argument("goal", type=int, help="Your Project Goal")
    parser.add_argument("--age", type=int, help="Your age", required=False)
    
    args = parser.parse_args()
    
    available_categories, available_subcategories, available_countries = get_valid_catoricals()
    
    # Validate category
    if args.category not in available_categories:
        print(f"Error: '{args.category}' is not a valid category. Available categories are: {available_categories}")
        return
    
    # Validate subcategory
    if args.subcategory not in available_subcategories:
        print(f"Error: '{args.subcategory}' is not a valid subcategory. Available subcategories are: {available_subcategories}")
        return
    
    # Validate country
    if args.country not in available_countries:
        print(f"Error: '{args.country}' is not a valid country. Available countries are: {available_countries}")
        return
    
    print(f"\nHello, you are interested in the {args.name} project!")
    print("There is a 90% probability that you're project will Succeed! Congratulations!!!!")
    if args.age:
        print(f"You are {args.age} years old.")

if __name__ == "__main__": 
    main()
    # python cli.py 'Project X' 'Film & Video' 'Documentary' 'United States' '2024-01-01' '2024-06-01' 100000