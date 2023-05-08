// This script handles the filters

// Checkmarks all who are in the parameters
function setCheckedState(inputElements, values) {
    inputElements.forEach((input) => {
      if (values.includes(input.value)) {
        input.checked = true;
      }
    });
  }
  
  function hideClearButton() {
    var clearButton = document.getElementById("clear-button");
    clearButton.style.display = 'none';
  }
  
  function showClearButton() {
    var clearButton = document.getElementById("clear-button");
    clearButton.style.display = 'block';
  }
  
  function hasActiveFilters(urlSearchParams) {
    const filterKeys = [
      "locations",
      "plant-types",
      "sun-exps",
      "waterings",
      "sortings",
      "sorting-order",
    ];
  
    return filterKeys.some((key) => urlSearchParams.has(key) && key !== "search_query");
  }

//Defaults
hideClearButton();

// Order By defaults to ascending
let defaultRadio = document.getElementById("order-1");
defaultRadio.checked = true;


const form = document.getElementById("filters-form");
const filterButtons = form.querySelectorAll('button[type="submit"]');

const urlSearchParams = new URLSearchParams(window.location.search);

// Extract all parameters from URL
const locations = urlSearchParams.getAll("locations");
const plantTypes = urlSearchParams.getAll("plant-types");
const sunExposures = urlSearchParams.getAll("sun-exps");
const waterings = urlSearchParams.getAll("waterings");
const sortings = urlSearchParams.getAll("sortings");
const orderBy = urlSearchParams.getAll("sorting-order");

// Fill checkmarks
setCheckedState(form.querySelectorAll('input[name="locations"]'), locations);
setCheckedState(form.querySelectorAll('input[name="plant-types"]'), plantTypes);
setCheckedState(form.querySelectorAll('input[name="sun-exps"]'), sunExposures);
setCheckedState(form.querySelectorAll('input[name="waterings"]'), waterings);
setCheckedState(form.querySelectorAll('input[name="sortings"]'), sortings);
setCheckedState(form.querySelectorAll('input[name="sorting-order"]'), orderBy);

if (hasActiveFilters(urlSearchParams)) {
    showClearButton();
} else {
    hideClearButton();
}

form.addEventListener("submit", function (event) {
    event.preventDefault();

    const clickedButtonValue = event.submitter.value;
    const searchParams = new URLSearchParams(window.location.search);

    if (clickedButtonValue === "clear") {
        form
            .querySelectorAll("input[type='checkbox'], input[type='radio']")
            .forEach((input) => {
                if (input.name != "search_query") {
                    searchParams.delete(input.name, input.value);
                }
            });
    }
    else if (clickedButtonValue === "all") {
        // Add values of all checkboxes and radio buttons to the searchParams
        form
            .querySelectorAll("input[type='checkbox'], input[type='radio']")
            .forEach((input) => {
                if (input.checked && input.name === "sorting-order") {
                    searchParams.delete(input.name);
                }
                if (input.checked && !searchParams.getAll(input.name).includes(input.value)) {
                    searchParams.append(input.name, input.value);
                }
                if (!input.checked && searchParams.getAll(input.name).includes(input.value)) {
                    searchParams.delete(input.name, input.value);
                }
            });
    } else {
        // Add values of checkboxes and radio buttons within the same category to the searchParams
        const categoryDiv = event.submitter.closest(".shop-widget");
        categoryDiv
            .querySelectorAll("input[type='checkbox'], input[type='radio']")
            .forEach((input) => {
                if (input.checked && input.name === "sorting-order") {
                    searchParams.delete(input.name);
                }

                if (input.checked && !searchParams.getAll(input.name).includes(input.value)) {
                    searchParams.append(input.name, input.value);
                }
                if (!input.checked && searchParams.getAll(input.name).includes(input.value)) {
                    searchParams.delete(input.name, input.value);
                }
            });
    }
    window.location.href = `/shop?${searchParams.toString()}`;
});