"""Quick viewer to display generated visualizations."""

import os
from PIL import Image
import matplotlib.pyplot as plt

VIZ_DIR = "visualizations"

def view_analytics():
    """Display all generated analytics visualizations."""
    
    # Change to visualization directory
    if not os.path.exists(VIZ_DIR):
        print(f"Visualization folder '{VIZ_DIR}' not found.")
        print("Run 'python visualize.py' first to generate visualizations.")
        return
    
    # Get all PNG files from visualizations folder
    viz_files = []
    for file in os.listdir(VIZ_DIR):
        if file.endswith('.png'):
            viz_files.append(os.path.join(VIZ_DIR, file))
    
    viz_files = sorted(viz_files)
    
    if not viz_files:
        print(f"No visualizations found in '{VIZ_DIR}' folder.")
        print("Run 'python visualize.py' first.")
        return
    
    print(f"\n📊 Found {len(viz_files)} visualizations in '{VIZ_DIR}' folder\n")
    
    for i, file in enumerate(viz_files, 1):
        print(f"{i}. {os.path.basename(file)}")
    
    print(f"\n{len(viz_files) + 1}. View all (grid view)")
    print(f"{len(viz_files) + 2}. Exit")
    
    while True:
        choice = input("\nEnter choice to view: ").strip()
        
        if choice == str(len(viz_files) + 2):
            break
        elif choice == str(len(viz_files) + 1):
            # Show all in grid
            n_images = len(viz_files)
            cols = 3
            rows = (n_images + cols - 1) // cols
            
            fig = plt.figure(figsize=(18, 6 * rows))
            
            for idx, file in enumerate(viz_files, 1):
                img = Image.open(file)
                ax = fig.add_subplot(rows, cols, idx)
                ax.imshow(img)
                ax.set_title(os.path.basename(file), fontsize=10)
                ax.axis('off')
            
            plt.tight_layout()
            plt.show()
        elif choice.isdigit() and 1 <= int(choice) <= len(viz_files):
            # Show single image
            file = viz_files[int(choice) - 1]
            img = Image.open(file)
            
            plt.figure(figsize=(12, 8))
            plt.imshow(img)
            plt.title(os.path.basename(file), fontsize=14, fontweight='bold')
            plt.axis('off')
            plt.tight_layout()
            plt.show()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    view_analytics()
