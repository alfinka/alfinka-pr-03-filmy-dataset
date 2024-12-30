import streamlit as st
import pandas as pd 
import altair as alt 

st.set_page_config(page_title="Analýza dataset Filmy", page_icon="🎥") 
st.title("🎥 Analýza dataset Filmy") 
st.write( 
    """     
    Táto aplikácia vizualizuje údaje z [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).     Ukazuje, ktorý filmový žáner mal v kinách za posledné roky najlepší výkon.      
    Stačí kliknúť na miniaplikácie nižšie a preskúmať ich!     
    """ 
)


@st.cache_data # @dekorátor pre načítanie a spracovanie veľkých dát
def load_data():     
    df = pd.read_csv("data/movies_genres_summary.csv")     
    return df 
df_filmy = load_data()

st.write(df_filmy)

zanre = st.multiselect(     
    "Zanre",     
    df_filmy.genre.unique(),     
    ["Action", "Adventure", "Biography", "Comedy", "Drama", "Horror"] 
    ) 
roky = st.slider(     
    "Roky",     
    1986,     
    2006,     
    (2000, 2016) 
)

# Filtrujte dátový rámec na základe vstupu widgetu a pretvorte ho.
df_filtered = df[(df["genre"].isin(genres)) & (df["year"].between(years[0], years[1]))] df_reshaped = df_filtered.pivot_table(     index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0 ) 
df_reshaped = df_reshaped.sort_values(by="year", ascending=False) 

# Zobrazte údaje ako tabuľku pomocou `st.dataframe`.



# Zobrazte údaje ako Altairovu tabuľku pomocou `st.altair_chart`.



# Pridajte stĺpcový graf s celkovými zárobkami podľa žánru.


# Pridanie textových popisov do stĺpcového grafu



# Pridajte koláčový graf pre rozdelenie zárobkov podľa žánru s percentami.



# Pridanie textových popisov do koláčového grafu s percentami vo vnútri





