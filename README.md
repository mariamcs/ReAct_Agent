Here's a **documentation-friendly version** of your personalized AI meal planning agent for your project `README.md`, API docs, or internal design documents:

---

# 🧠 Personalized AI Meal Planning Agent

This project is an **intelligent meal planning agent** that dynamically generates and adjusts daily meal plans based on individual client goals, dietary preferences, and feedback. It uses a macro-driven database of meals and ensures each user hits their nutrition targets—especially protein intake.

---

## 📌 Key Features

* 🔍 **Personalized Meal Plans**: 4 meals/day tailored to client’s weight, height, activity level, and fitness goal (fat loss, muscle gain, or maintenance)
* 🌱 **Diet-Aware Filtering**: Supports preferences like vegetarian, vegan, pescatarian, or ingredient-specific dislikes (e.g., no fish, no dairy)
* ⚖️ **Dynamic Macro Calculation**: Automatically adjusts calorie, protein, fat, and carb targets based on goals
* 🔁 **Interactive Feedback Loop**: If a client dislikes a meal, the agent will replan that meal and re-balance the macros
* 🧮 **Protein Goal Enforcement**: Ensures daily protein target is 1.0–1.2g per pound of body weight

---

## 🧠 Agent Workflow

```
1. Client provides input:
   - Weight, height, activity level, and goal
   - Dietary type (e.g., vegan)
   - Ingredients to avoid (e.g., mushrooms, fish)

2. Agent calculates target macros:
   - Calories based on TDEE and goal
   - Protein: 1–1.2g/lb of body weight
   - Fat: ~25% of daily calories
   - Carbs: remainder

3. Agent selects 4 meals from a meal database:
   - Matches dietary rules
   - Distributes protein across meals
   - Meets macro targets

4. Agent presents the meal plan and requests feedback:
   - Client can approve or reject meals
   - Disliked meals are swapped with alternatives
   - Macros are rebalanced as needed
```

---

## 🛠️ Technologies & Tools

| Component                   | Description                                      |
| --------------------------- | ------------------------------------------------ |
| **Meal Database**           | Meals with macros, ingredients, and dietary tags |
| **Macro Calculator**        | Python function to compute TDEE and macro goals  |
| **Agent Logic**             | LLM / rules-based planner with feedback loop     |
| **UI (optional)**           | Streamlit or CLI interface for interactivity     |
| **Vector Store (optional)** | For memory or ingredient-level retrieval         |

---

## 📥 Example Client Input

```json
{
  "weight": 150,
  "height": 5.5,
  "goal": "muscle gain",
  "diet": "vegetarian",
  "activity_level": "moderate",
  "dislikes": ["eggplant", "tofu"]
}
```

---

## ⚙️ Macro Target Example (150 lbs client, muscle gain)

```python
protein = 1.2 * 150  # = 180g
calories = TDEE + 250  # ~Maintenance + surplus
fat = 0.25 * calories / 9
carbs = remaining calories
```

---

## 🧪 Sample Agent Response

```
Here is your suggested meal plan:

1. Breakfast: Protein Oats with Almond Butter (P: 30g, C: 45g, F: 10g)
2. Lunch: Lentil Salad with Avocado (P: 35g, C: 50g, F: 15g)
3. Snack: Greek Yogurt with Berries (P: 25g, C: 15g, F: 5g)
4. Dinner: Chickpea Stir-Fry with Quinoa (P: 40g, C: 55g, F: 12g)

Would you like to make any swaps or changes?
```

---

## 📈 Future Improvements

* [ ] Add support for ingredient-level substitutions
* [ ] Integrate meal image previews and barcode scanning
* [ ] Enable long-term diet tracking and logging
* [ ] Integrate with LLMs for natural language interaction

---

## 🧑‍💻 Author

Created by [Your Name](https://github.com/yourusername)

---

Let me know if you’d like this formatted as a Jupyter notebook, converted into an API doc, or turned into an actual prototype repo!
