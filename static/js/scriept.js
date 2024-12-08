// Sample Data (Including images)
const places = [
    { name: "Store Street Espresso", address: "245 Hammersmith Road", rating: 97, image: "https://via.placeholder.com/300x200?text=Place+1" },
    { name: "Arancina", address: "19 Pembridge Road", rating: 96, image: "https://via.placeholder.com/300x200?text=Place+2" },
    { name: "Building Centre", address: "26 Store Street", rating: 93, image: "https://via.placeholder.com/300x200?text=Place+3" },
    { name: "Well Bean Co - Café", address: "1-2 Upper Dock Walk", rating: 92, image: "https://via.placeholder.com/300x200?text=Place+4" }
];

// Function to Load Places Dynamically
const placesList = document.getElementById("places-list");

places.forEach(place => {
    const placeElement = document.createElement("div");
    placeElement.classList.add("place");

    placeElement.innerHTML = `
        <img src="${place.image}" alt="${place.name}">
        <div class="place-info">
            <h3>${place.name}</h3>
            <p>${place.address}</p>
            <p class="rating">Rating: ${place.rating}%</p>
        </div>
    `;

    placesList.appendChild(placeElement);
});
