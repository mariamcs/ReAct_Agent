{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPzEHA6CctDJw4GScb5BncP",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mariamcs/ReAct_Agent/blob/main/meal_plan_generator.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 430
        },
        "id": "uaEeh3D6SjAh",
        "outputId": "84f3601e-1b44-454d-89f6-4543d10b131f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "✅ meal_database.csv created\n",
            "✅ client_database.csv created\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'client_profile'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipython-input-1-2013843788.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     62\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     63\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mrandom\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 64\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mclient_profile\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcalculate_macros\u001b[0m  \u001b[0;31m# Import your macro calculator\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     65\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     66\u001b[0m \u001b[0;31m# Load meal and client data\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'client_profile'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ],
      "source": [
        "import pandas as pd\n",
        "import random\n",
        "\n",
        "# -------------------------------\n",
        "# 🍽️ Sample Meal Database (20 meals)\n",
        "# -------------------------------\n",
        "meal_data = [\n",
        "    {\"meal_id\": 1, \"meal_name\": \"Grilled Chicken with Quinoa\", \"protein\": 35, \"carbs\": 40, \"fat\": 10, \"calories\": 430, \"diet\": \"omnivore\", \"ingredients\": [\"chicken\", \"quinoa\", \"spinach\"]},\n",
        "    {\"meal_id\": 2, \"meal_name\": \"Tofu Stir-Fry\", \"protein\": 28, \"carbs\": 35, \"fat\": 12, \"calories\": 410, \"diet\": \"vegan\", \"ingredients\": [\"tofu\", \"broccoli\", \"carrots\"]},\n",
        "    {\"meal_id\": 3, \"meal_name\": \"Lentil Soup\", \"protein\": 24, \"carbs\": 30, \"fat\": 8, \"calories\": 360, \"diet\": \"vegetarian\", \"ingredients\": [\"lentils\", \"tomato\", \"onion\"]},\n",
        "    {\"meal_id\": 4, \"meal_name\": \"Salmon and Sweet Potato\", \"protein\": 32, \"carbs\": 42, \"fat\": 15, \"calories\": 480, \"diet\": \"pescatarian\", \"ingredients\": [\"salmon\", \"sweet potato\", \"greens\"]},\n",
        "    {\"meal_id\": 5, \"meal_name\": \"Vegan Burrito Bowl\", \"protein\": 20, \"carbs\": 50, \"fat\": 14, \"calories\": 470, \"diet\": \"vegan\", \"ingredients\": [\"black beans\", \"rice\", \"guacamole\"]},\n",
        "    {\"meal_id\": 6, \"meal_name\": \"Egg Omelet with Veggies\", \"protein\": 27, \"carbs\": 10, \"fat\": 18, \"calories\": 350, \"diet\": \"vegetarian\", \"ingredients\": [\"eggs\", \"pepper\", \"spinach\"]},\n",
        "    {\"meal_id\": 7, \"meal_name\": \"Turkey Chili\", \"protein\": 36, \"carbs\": 30, \"fat\": 10, \"calories\": 420, \"diet\": \"omnivore\", \"ingredients\": [\"ground turkey\", \"beans\", \"tomato\"]},\n",
        "    {\"meal_id\": 8, \"meal_name\": \"Greek Yogurt Parfait\", \"protein\": 22, \"carbs\": 20, \"fat\": 5, \"calories\": 260, \"diet\": \"vegetarian\", \"ingredients\": [\"greek yogurt\", \"berries\", \"honey\"]},\n",
        "    {\"meal_id\": 9, \"meal_name\": \"Tempeh Salad\", \"protein\": 25, \"carbs\": 15, \"fat\": 10, \"calories\": 300, \"diet\": \"vegan\", \"ingredients\": [\"tempeh\", \"lettuce\", \"cucumber\"]},\n",
        "    {\"meal_id\": 10, \"meal_name\": \"Shrimp & Rice Bowl\", \"protein\": 30, \"carbs\": 38, \"fat\": 8, \"calories\": 400, \"diet\": \"pescatarian\", \"ingredients\": [\"shrimp\", \"rice\", \"broccoli\"]},\n",
        "    {\"meal_id\": 11, \"meal_name\": \"Cottage Cheese Bowl\", \"protein\": 28, \"carbs\": 12, \"fat\": 10, \"calories\": 310, \"diet\": \"vegetarian\", \"ingredients\": [\"cottage cheese\", \"berries\", \"nuts\"]},\n",
        "    {\"meal_id\": 12, \"meal_name\": \"Baked Tilapia & Greens\", \"protein\": 33, \"carbs\": 8, \"fat\": 7, \"calories\": 290, \"diet\": \"pescatarian\", \"ingredients\": [\"tilapia\", \"kale\", \"olive oil\"]},\n",
        "    {\"meal_id\": 13, \"meal_name\": \"Avocado Toast with Egg\", \"protein\": 20, \"carbs\": 25, \"fat\": 15, \"calories\": 350, \"diet\": \"vegetarian\", \"ingredients\": [\"egg\", \"avocado\", \"toast\"]},\n",
        "    {\"meal_id\": 14, \"meal_name\": \"Protein Pancakes\", \"protein\": 30, \"carbs\": 30, \"fat\": 8, \"calories\": 360, \"diet\": \"vegetarian\", \"ingredients\": [\"protein powder\", \"oats\", \"banana\"]},\n",
        "    {\"meal_id\": 15, \"meal_name\": \"Veggie Wrap\", \"protein\": 18, \"carbs\": 40, \"fat\": 9, \"calories\": 370, \"diet\": \"vegan\", \"ingredients\": [\"wrap\", \"lettuce\", \"hummus\"]},\n",
        "    {\"meal_id\": 16, \"meal_name\": \"Beef & Broccoli\", \"protein\": 35, \"carbs\": 25, \"fat\": 14, \"calories\": 420, \"diet\": \"omnivore\", \"ingredients\": [\"beef\", \"broccoli\", \"soy sauce\"]},\n",
        "    {\"meal_id\": 17, \"meal_name\": \"Stuffed Peppers\", \"protein\": 28, \"carbs\": 32, \"fat\": 10, \"calories\": 400, \"diet\": \"omnivore\", \"ingredients\": [\"ground beef\", \"pepper\", \"rice\"]},\n",
        "    {\"meal_id\": 18, \"meal_name\": \"Protein Smoothie\", \"protein\": 32, \"carbs\": 18, \"fat\": 6, \"calories\": 310, \"diet\": \"vegetarian\", \"ingredients\": [\"protein powder\", \"almond milk\", \"banana\"]},\n",
        "    {\"meal_id\": 19, \"meal_name\": \"Hummus Bowl\", \"protein\": 22, \"carbs\": 35, \"fat\": 12, \"calories\": 390, \"diet\": \"vegan\", \"ingredients\": [\"hummus\", \"quinoa\", \"cucumber\"]},\n",
        "    {\"meal_id\": 20, \"meal_name\": \"Egg Fried Rice\", \"protein\": 24, \"carbs\": 44, \"fat\": 10, \"calories\": 420, \"diet\": \"vegetarian\", \"ingredients\": [\"egg\", \"rice\", \"peas\"]},\n",
        "]\n",
        "\n",
        "df_meals = pd.DataFrame(meal_data)\n",
        "df_meals.to_csv(\"meal_database.csv\", index=False)\n",
        "print(\"✅ meal_database.csv created\")\n",
        "\n",
        "# -------------------------------\n",
        "# 🧍 Sample Client Database (100 clients)\n",
        "# -------------------------------\n",
        "\n",
        "genders = [\"male\", \"female\"]\n",
        "goals = [\"fat loss\", \"muscle gain\", \"maintenance\"]\n",
        "diets = [\"omnivore\", \"vegetarian\", \"vegan\", \"pescatarian\"]\n",
        "activity_levels = [\"sedentary\", \"light\", \"moderate\", \"active\", \"very active\"]\n",
        "\n",
        "def random_client(i):\n",
        "    return {\n",
        "        \"client_id\": i,\n",
        "        \"weight_lbs\": random.randint(120, 220),\n",
        "        \"height_in\": random.randint(60, 75),\n",
        "        \"age\": random.randint(20, 55),\n",
        "        \"gender\": random.choice(genders),\n",
        "        \"activity_level\": random.choice(activity_levels),\n",
        "        \"goal\": random.choice(goals),\n",
        "        \"diet\": random.choice(diets),\n",
        "        \"dislikes\": random.sample([\"fish\", \"eggplant\", \"tofu\", \"mushroom\", \"dairy\", \"beef\"], k=random.randint(0, 2))\n",
        "    }\n",
        "\n",
        "clients = [random_client(i) for i in range(1, 101)]\n",
        "df_clients = pd.DataFrame(clients)\n",
        "df_clients.to_csv(\"client_database.csv\", index=False)\n",
        "print(\"✅ client_database.csv created\")\n",
        "\n",
        "\n",
        "import pandas as pd\n",
        "import random\n",
        "from client_profile import calculate_macros  # Import your macro calculator\n",
        "\n",
        "# Load meal and client data\n",
        "df_meals = pd.read_csv(\"meal_database.csv\")\n",
        "df_clients = pd.read_csv(\"client_database.csv\")\n",
        "\n",
        "\n",
        "def filter_meals(client_row):\n",
        "    # Diet and dislikes filtering\n",
        "    diet_type = client_row[\"diet\"]\n",
        "    dislikes = client_row[\"dislikes\"].strip(\"[]\").replace(\"'\", \"\").split(\", \")\n",
        "\n",
        "    filtered = df_meals[df_meals[\"diet\"].isin([diet_type, \"vegan\", \"vegetarian\", \"pescatarian\", \"omnivore\"])]\n",
        "\n",
        "    def not_contains_dislikes(ingredients_str):\n",
        "        ingredients = eval(ingredients_str) if isinstance(ingredients_str, str) else ingredients_str\n",
        "        return all(dislike.lower() not in [i.lower() for i in ingredients] for dislike in dislikes if dislike)\n",
        "\n",
        "    return filtered[filtered[\"ingredients\"].apply(not_contains_dislikes)]\n",
        "\n",
        "\n",
        "def generate_plan(client_row):\n",
        "    # Step 1: Calculate target macros\n",
        "    macros = calculate_macros(\n",
        "        weight_lbs=client_row[\"weight_lbs\"],\n",
        "        height_in=client_row[\"height_in\"],\n",
        "        age=client_row[\"age\"],\n",
        "        gender=client_row[\"gender\"],\n",
        "        activity_level=client_row[\"activity_level\"],\n",
        "        goal=client_row[\"goal\"]\n",
        "    )\n",
        "\n",
        "    target_p = macros[\"protein\"]\n",
        "    target_c = macros[\"carbs\"]\n",
        "    target_f = macros[\"fat\"]\n",
        "\n",
        "    meals = filter_meals(client_row)\n",
        "\n",
        "    best_plan = None\n",
        "    min_error = float(\"inf\")\n",
        "\n",
        "    # Try random 4-meal combinations to find closest match\n",
        "    for _ in range(1000):\n",
        "        sample = meals.sample(4)\n",
        "        total_p = sample[\"protein\"].sum()\n",
        "        total_c = sample[\"carbs\"].sum()\n",
        "        total_f = sample[\"fat\"].sum()\n",
        "\n",
        "        # Check how close we are to target\n",
        "        error = abs(total_p - target_p) + abs(total_c - target_c) + abs(total_f - target_f)\n",
        "\n",
        "        if error < min_error:\n",
        "            best_plan = sample\n",
        "            min_error = error\n",
        "\n",
        "        if error < 0.05 * (target_p + target_c + target_f):  # early stopping if close enough\n",
        "            break\n",
        "\n",
        "    return best_plan, macros\n",
        "\n",
        "\n",
        "# Example: generate plan for client 0\n",
        "if __name__ == \"__main__\":\n",
        "    client = df_clients.iloc[0]\n",
        "    print(f\"\\n🧍 Generating plan for client {client['client_id']}...\\n\")\n",
        "    plan, targets = generate_plan(client)\n",
        "\n",
        "    print(\"🎯 Macro Targets:\", targets)\n",
        "    print(\"\\n🍽️ Meal Plan:\\n\", plan[[\"meal_name\", \"protein\", \"carbs\", \"fat\", \"calories\", \"ingredients\"]])\n",
        "    print(\"\\n✅ Total Macros:\")\n",
        "    print(\"Protein:\", plan[\"protein\"].sum(), \"g\")\n",
        "    print(\"Carbs:\", plan[\"carbs\"].sum(), \"g\")\n",
        "    print(\"Fat:\", plan[\"fat\"].sum(), \"g\")\n"
      ]
    }
  ]
}