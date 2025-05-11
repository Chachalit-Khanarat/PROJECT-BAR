# Bartender Rush – Game Overview



## Project Overview

*Bartender Rush* is a fast-paced simulation game where the player takes on the role of a bartender working through nightly rush hours. Each customer comes with vague descriptions of drinks, and the player must interpret these requests under time pressure.

The game features multiple customer types including regulars, locals, and random visitors, each with unique behavior and patience levels. Player efficiency and drink accuracy influence income and customer satisfaction.

---

## Programming Development

### 2.1 Game Concept

Players are tasked with identifying drinks based on incomplete customer descriptions. Speed and accuracy are key. The game takes inspiration from **VA-11 Hall-A**, combining drink-making with character-driven interaction.

### 2.2 Object-Oriented Programming Implementation

The game is structured with a modular OOP approach. Core components include:

- **`Draw_Manager`**  
  Handles all rendering operations including UI, text, and animations.

- **`Drinks`**  
  Loads and manages all drink data using `pandas`. Handles logic for parsing drink recipes and matching player input.

- **`Customer`**  
  Base class representing a customer. Includes properties like mood, patience, and order. Can be extended for different customer types.

- **`Game_Ui`**  
  Manages the user interface layout and updates the game state visually.

- **`Mixer`**  
  Tracks ingredients currently being mixed by the player and compares them against drink recipes.

---

## UML Diagram

The following UML class diagram illustrates the relationship between the main components:

![UML Diagram](UML.png)