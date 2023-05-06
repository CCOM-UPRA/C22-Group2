        //This script caps the amount of items you can buy
        document.addEventListener("DOMContentLoaded", function () {
            function enforceMinMax(element) {
                if (element.value !== "") {
                    if (parseInt(element.value) < parseInt(element.min)) {
                        element.value = element.min;
                    }
                    if (parseInt(element.value) > parseInt(element.max)) {
                        element.value = element.max;
                    }
                }
            }

            function decreaseQuantity(event) {
                let inputElement = event.target.closest('.product-action').querySelector(".custom-quantity-input");
                let currentValue = parseInt(inputElement.value);
                if (currentValue > parseInt(inputElement.min)) {
                    inputElement.value = currentValue - 1;
                }
            }

            function increaseQuantity(event) {
                let inputElement = event.target.closest('.product-action').querySelector(".custom-quantity-input");
                let currentValue = parseInt(inputElement.value);
                if (currentValue < parseInt(inputElement.max)) {
                    inputElement.value = currentValue + 1;
                }
            }

            let minusButtons = document.querySelectorAll(".custom-quantity-minus");
            let plusButtons = document.querySelectorAll(".custom-quantity-plus");
            let inputElements = document.querySelectorAll(".custom-quantity-input");

            minusButtons.forEach(function (minusButton) {
                minusButton.addEventListener("click", decreaseQuantity);
            });

            plusButtons.forEach(function (plusButton) {
                plusButton.addEventListener("click", increaseQuantity);
            });

            inputElements.forEach(function (inputElement) {
                inputElement.addEventListener("keyup", function () {
                    enforceMinMax(this);
                });
            });
        });