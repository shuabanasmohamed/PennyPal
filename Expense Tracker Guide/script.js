let expenses = [];

function addExpense() {
    const amount = parseFloat(document.getElementById('amount').value);
    const category = document.getElementById('category').value;
    const description = document.getElementById('description').value;

    if (isNaN(amount) || amount <= 0) {
        alert("Please enter a valid positive number for the amount.");
        return;
    }

    if (description.trim() === "") {
        alert("Please enter a description.");
        return;
    }

    expenses.push({ amount, category, description });
    document.getElementById('amount').value = "";
    document.getElementById('description').value = "";
    displaySummary();
}

function displaySummary() {
    let totalAmount = 0;
    let categoryTotals = {};

    expenses.forEach(expense => {
        totalAmount += expense.amount;
        if (categoryTotals[expense.category]) {
            categoryTotals[expense.category] += expense.amount;
        } else {
            categoryTotals[expense.category] = expense.amount;
        }
    });

    let summaryHtml = `<p>Total Amount Spent: $${totalAmount.toFixed(2)}</p>`;
    for (const [category, total] of Object.entries(categoryTotals)) {
        summaryHtml += `<p>${category}: $${total.toFixed(2)}</p>`;
    }

    summaryHtml += "<h3>All Expenses:</h3>";
    expenses.forEach(expense => {
        summaryHtml += `<p>${expense.amount.toFixed(2)}: ${expense.category} - ${expense.description}</p>`;
    });

    document.getElementById('summary').innerHTML = summaryHtml;
}