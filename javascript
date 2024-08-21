const recommendations = {
    action: ["Mad Max: Fury Road", "John Wick", "Die Hard", "The Dark Knight"],
    comedy: ["The Hangover", "Step Brothers", "Superbad", "Anchorman"],
    drama: ["The Godfather", "Shawshank Redemption", "Forrest Gump", "Fight Club"],
    horror: ["The Conjuring", "Get Out", "A Nightmare on Elm Street", "It"],
    "sci-fi": ["Inception", "The Matrix", "Interstellar", "Blade Runner 2049"]
};

const randrecommendations = {
    random: [
        "Mad Max: Fury Road", "John Wick", "Die Hard", "The Dark Knight",
        "The Hangover", "Step Brothers", "Superbad", "Anchorman",
        "The Godfather", "Shawshank Redemption", "Forrest Gump", "Fight Club",
        "The Conjuring", "Get Out", "A Nightmare on Elm Street", "It",
        "Inception", "The Matrix", "Interstellar", "Blade Runner 2049"
    ]
};

document.getElementById("recommendButton").onclick = function() {
    const genre = document.getElementById("genre").value;
    const movies = recommendations[genre];
    const randomMovie = movies[Math.floor(Math.random() * movies.length)];
    
    document.getElementById("recommendation").textContent = `We recommend you to watch: ${randomMovie}`;
};

document.getElementById("randrecommendButton").onclick = function() {
    const movies = randrecommendations["random"];
    const randomMovie = movies[Math.floor(Math.random() * movies.length)];
    
    document.getElementById("recommendation").textContent = `We recommend you to watch: ${randomMovie}`;
};
