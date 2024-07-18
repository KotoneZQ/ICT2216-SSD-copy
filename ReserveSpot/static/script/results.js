function removeCategory(categoryId) {
    // Remove the category box
    const categoryBox = document.getElementById(categoryId);
    categoryBox.parentNode.removeChild(categoryBox);

    // Remove the corresponding search results
    const searchResults = document.getElementById('search-results');
    // Assuming the results are dynamically loaded with IDs that match the category box ID pattern
    const resultsToRemove = searchResults.querySelectorAll(`.result[data-category='${categoryId}']`);
    resultsToRemove.forEach(function(result) {
        result.parentNode.removeChild(result);
    })
}

function openFilterOptions() {
    const filterOptions = document.getElementById("filterOptions");
    filterOptions.style.display = filterOptions.style.display === "block" ? "none" : "block";
}

function closeFilterOptions() {
    const filterOptions = document.getElementById("filterOptions");
    filterOptions.style.display = "none";
}

function applySettings() {
    // Retrieve the selected settings
    const sortByPrice = document.querySelector('input[name="sortByPriceAsc"]').checked;
    const sortByPriceDesc = document.querySelector('input[name="sortByPriceDesc"]').checked;
    const sortByRating = document.querySelector('input[name="sortByRatingAsc"]').checked;
    const sortByRatingDesc = document.querySelector('input[name="sortByRatingDesc"]').checked;

    // Add further logic to save the settings (e.g., send to server, store in localStorage, etc.)
    
    // Close the filter options after saving (optional)
    closeFilterOptions();
}
