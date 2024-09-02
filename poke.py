import requests
import streamlit as st

# Function to fetch Pokémon data from the PokeAPI
def get_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to display Pokémon stats and image
def display_stats_and_image(pokemon, title):
    st.subheader(title)
    if pokemon:
        st.image(pokemon['sprites']['front_default'], width=150)  # Display the Pokémon image
        st.write(f"**Name:** {pokemon['name'].capitalize()}")
        stats = {stat['stat']['name']: stat['base_stat'] for stat in pokemon['stats']}
        for stat_name, stat_value in stats.items():
            st.write(f"**{stat_name.capitalize()}:** {stat_value}")
    else:
        st.error("Pokémon not found!")

# Streamlit App
st.title("Pokémon Stats Comparison")
pokemon_name = "giratina"
pokemon = get_pokemon_data(pokemon_name)
if pokemon:
    print(f"Found {pokemon['name'].capitalize()}!")
else:
    print("Giratina not found!")


pokemon1_name = st.text_input("Enter the name of the first Pokémon:")
pokemon2_name = st.text_input("Enter the name of the second Pokémon:")

if st.button("Compare"):
    pokemon1 = get_pokemon_data(pokemon1_name)
    pokemon2 = get_pokemon_data(pokemon2_name)

    col1, col2 = st.columns(2)

    with col1:
        display_stats_and_image(pokemon1, "First Pokémon")

    with col2:
        display_stats_and_image(pokemon2, "Second Pokémon")
