const quotes = {
    happy: ["Stay positive!", "Happiness is a choice!", "Smile, it's free therapy!"],
    sad: ["Tears are words that need to be written.", "It's okay to feel sad.", "This too shall pass."],
    anxious: ["Take a deep breath.", "You're stronger than your anxiety.", "Calmness is the cradle of power."],
    depressed: ["You are not alone.", "It's okay to not be okay.", "Hope is real."],
    angry: ["Take a moment to breathe.", "Anger is a momentary madness.", "Think before you speak."],
};

function showQuote(feeling) {
    const quoteBox = document.getElementById('quoteBox');
    const quoteText = document.getElementById('quote');
    const feelingText = document.getElementById('feelingText');

    // Hide feeling options
    document.querySelector('.emotions').style.display = 'none';
    feelingText.style.display = 'none';

    // Get a random quote
    const randomQuote = quotes[feeling][Math.floor(Math.random() * quotes[feeling].length)];
    quoteText.textContent = randomQuote;

    // Show quote box with animation
    quoteBox.classList.add('show');
    document.querySelector('.back-button').style.display = 'block'; // Show the back button
}

function goBack() {
    const quoteBox = document.getElementById('quoteBox');
    const feelingText = document.getElementById('feelingText');

    // Hide the quote box
    quoteBox.classList.remove('show');
    
    // Show feeling options again
    document.querySelector('.emotions').style.display = 'block';
    feelingText.style.display = 'block';
    document.querySelector('.back-button').style.display = 'none'; // Hide the back button
}
