import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class DataVisualizer:
    def __init__(self, output_dir="data/graph"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def load_customer_data(self):
        self.customer_data = pd.read_csv("data/csv/cus.csv").sort_values(by="name")

    def load_player_data(self):
        self.player_data = pd.read_csv("data/csv/player.csv").sort_values(by="_PlayerData__player_id")
    
    def load_item_data(self):
        self.item_data = pd.read_csv("data/csv/items.csv").sort_values(by="Item Name")

    def plot_customer_frequency(self):
        plt.figure(figsize=(12, 10))
        self.customer_data["name"].hist(label="Customer Frequency")
        plt.xticks(rotation=90, ha="center")
        plt.xlabel("Customer Names")
        plt.ylabel("Frequency")
        plt.title("Histogram of Customer Frequency")
        plt.savefig(os.path.join(self.output_dir, "customer_frequency.png"), bbox_inches='tight')
    
    def plot_customer_frequency_pie(self):
        plt.figure(figsize=(10, 8))
        customer_counts = self.customer_data["name"].value_counts()
        customer_counts.plot(kind="pie", autopct="%1.1f%%", startangle=140, colormap="viridis")
        plt.ylabel("")  # Remove y-axis label for better appearance
        plt.title("Pie Chart of Customer Frequency")
        plt.savefig(os.path.join(self.output_dir, "customer_frequency_pie.png"), bbox_inches='tight')
        plt.close()

    def plot_customer_satisfaction(self):
        plt.figure(figsize=(12, 10))
        self.customer_data[self.customer_data["satisfaction"] == 1].groupby("name")["satisfaction"].count().plot(kind="bar", label="Customer Satisfaction")
        plt.xticks(rotation=90, ha="center")
        plt.xlabel("Customer Satisfaction Levels")
        plt.ylabel("Frequency")
        plt.title("Bar Plot of Customer Satisfaction Levels")
        plt.savefig(os.path.join(self.output_dir, "customer_satisfaction.png"), bbox_inches='tight')

    def plot_average_money_per_day(self):
        plt.figure(figsize=(12, 8))
        avg_money_per_day = self.player_data.groupby("_PlayerData__day")["_PlayerData__money"].mean().reset_index(name="average_money")
        sns.barplot(x="_PlayerData__day", y="average_money", data=avg_money_per_day, palette="coolwarm", label="Average Money per Day")
        plt.xlabel("Day")
        plt.ylabel("Average Money")
        plt.title("Bar Plot of Average Money per Day")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.output_dir, "average_money_per_day.png"), bbox_inches='tight')
        plt.close()

    def plot_player_money_vs_rent(self, player_id):
        player_data = self.player_data[self.player_data["_PlayerData__player_id"]//1000 == player_id]
        if player_data.empty:
            print(f"No data found for player ID: {player_id}")
            return

        # Calculate rent money
        days = player_data["_PlayerData__day"].values
        rent_money = [150 * (1.75 ** day) for day in days]

        plt.figure(figsize=(12, 8))
        sns.lineplot(x=player_data["_PlayerData__day"], y=player_data["_PlayerData__money"], label="Player Money", marker="o")
        sns.lineplot(x=days, y=rent_money, label="Rent Money", marker="o")
        plt.xlabel("Day")
        plt.ylabel("Money")
        plt.title(f"Player Money vs Rent Money for Player {player_id}")
        plt.legend(title="Metrics")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.output_dir, f"player_{player_id}_money_vs_rent.png"), bbox_inches='tight')
        plt.close()
    
    def plot_average_player_money_vs_rent(self):
        avg_player_data = self.player_data.groupby("_PlayerData__day")["_PlayerData__money"].mean().reset_index(name="average_money")
        
        # Calculate average rent money
        days = avg_player_data["_PlayerData__day"].values
        avg_rent_money = [150 * (1.75 ** day) for day in days]

        plt.figure(figsize=(12, 8))
        sns.lineplot(x=avg_player_data["_PlayerData__day"], y=avg_player_data["average_money"], label="Average Player Money", marker="o")
        sns.lineplot(x=days, y=avg_rent_money, label="Average Rent Money", marker="o")
        plt.xlabel("Day")
        plt.ylabel("Money")
        plt.title("Average Player Money vs Average Rent Money Over Days")
        plt.legend(title="Metrics")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(self.output_dir, "average_player_money_vs_rent.png"), bbox_inches='tight')
        plt.close()


    def plot_item_purchase_frequency(self):
        plt.figure(figsize=(12, 8))
        item_purchase_data = self.item_data.groupby("Item Name")["times bought"].sum().reset_index()
        sns.barplot(x="Item Name", y="times bought", data=item_purchase_data, palette="viridis")
        plt.xticks(rotation=90, ha="center")
        plt.xlabel("Item Name")
        plt.ylabel("Times Bought")
        plt.title("Bar Plot of Item Purchase Frequency")
        plt.savefig(os.path.join(self.output_dir, "item_purchase_frequency.png"), bbox_inches='tight')
        plt.close()

    def plot_item_correlation(self):
        plt.figure(figsize=(12, 8))
        sns.lineplot(x="Item Name", y="times bought", data=self.item_data, label="Times Bought", marker="o")
        sns.lineplot(x="Item Name", y="Bonus", data=self.item_data, label="Bonus", marker="o")
        plt.xlabel("Item Name")
        plt.ylabel("Values")
        plt.title("Comparison of Times Bought and Bonus for Items")
        plt.xticks(rotation=90, ha="center")
        plt.legend(title="Metrics")
        plt.savefig(os.path.join(self.output_dir, "item_correlation.png"), bbox_inches='tight')
        plt.close()

    def run_all_methods(self):
        self.load_customer_data()
        self.load_player_data()
        self.load_item_data()
        self.plot_customer_frequency_pie()
        self.plot_customer_frequency()
        self.plot_customer_satisfaction()
        self.plot_average_money_per_day()
        self.plot_item_purchase_frequency()
        self.plot_item_correlation()
        self.plot_average_player_money_vs_rent()

if __name__ == "__main__":
    visualizer = DataVisualizer()
    visualizer.run_all_methods()