// Function to print decimal palindromic number 
void generatePalindromes(int n) 
{ 
    int number; 
  
    // Run two times for odd and even length palindromes 
    for (int j = 0; j < 2; j++) 
    { 
        // Creates palindrome numbers with first half as i.  
        // Value of j decided whether we need an odd length 
        // of even length palindrome. 
        int i = 1; 
        while ((number = createPalindrome(i, 10, j % 2)) < n) 
        { 
            cout << number << " "; 
            i++; 
        } 
    } 
} 