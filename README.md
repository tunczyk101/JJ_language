# JJ_language





## KONCEPCJA
W ramach projektu stworzono interpreter wykorzystujący język programowania Python oraz bibliotekę AntLR.
Główny koncept języka to ułatwienie stosowania „Single exit-point rule” przy jednoczesnym zachowaniu czytelności oraz strukturalności kodu.
Aby osiągnąć cel skorzystano z idei znanej z programowania funkcyjnego – Function Guards, która występuje w językach takich jak Haskell oraz Elixir.

## ZMIENNE
- Inicjalizowanie zmiennych:
    - Za pomocą słowa let, nazwy zmienner oraz {wartość zmiennej}
        Np.  	let a { 10 };
        let b { true };
    - W ramach języka dostępne są typy:
        - int 	np. let a { 1 };
        - float	np. let b { 2.0 };
        - bool	np. let c { false };
    - Zmienne domyślnie są niemutowalne, aby mogły być mutable należy je zainicjować za pomocą dodatkowego słowa mut (jak poniżej)
    Np.	let mut d { 1.0 };	- zmienna mutowalna
    let e { 1.0 };		- zmienna niemutowalna
- Silna typizacja – typ ustalany na podstawie formy wartości zmiennej w „{}” (jak w podpunkcie o dostępnych typach)
- Możliwa konwersja typów za pomocą wyrażenia zmienna/wartość as typ
    - println(1 as bool); &emsp; &emsp; true
    - let mut x { 1 };\ 
        x = 2.4 as int;\
        println(x); &emsp;&emsp;&emsp; ***2***\
        println(x as float);&emsp;&emsp; ***2.0***
- Odwoływanie się do niezadeklarowanej zmiennej kończy się błędem
## OPERATORY
•	Operatory równości: x != y oraz  x == y
•	Dodawanie/odejmowanie: x + y oraz x – y
•	Mnożenie/dzielenie: x * y oraz x / y
•	Suma logiczna: x && y
•	Alternatywa: x || y
•	Negacja: !x
## FUNKCJE
•	Deklarowanie funkcji – budowa blokowa
    Deklaracja składa się z:
    o	Bloku obowiązkowego:
    Słowo kluczowe func oraz nazwa funkcji
    o	Bloki opcjonalne
        - Argumenty funkcji 
        - Warunki względem argumentu
        - Blok operacji
        - Zwracanie wartości
•	Przekazywane wartości - analogiczne jak w przypadku zmiennych, aby można je było modyfikować należy przed nazwą zmiennej użyć słowa mut.
'''
Np.
func add
with mut x
{
    	    x = x + 2; 
}
'''
•	Wymagana jest domyślna wersja funkcji
•	Można wielokrotnie deklarować tę samą funkcję, każda następna re-deklaracja nadpisuje sposób działania funkcji jedynie dla argumentów dla których jest zdefiniowana, dla pozostałych obowiązuje jedna z wcześniejszych wersji.
•	Zgodnie z ideą języka funkcje powinny być tworzone od najogólniejszych przypadków a kończąc na szczególnych. Funkcja domyślna ma występować w kodzie jako pierwsza deklaracja danej funkcji.
•	Przykłady
'''
func fib                        // definicja funkcji
with x                          // argumenty funkcji
when x >= 0                     // GUARDY na funkcje
returns fib(x-1) + fib(x-2)     // rekurencja 

func fib
with x
when x <= 1 
returns 0                       // Single exit point

func fib
with x
when x == 1
returns 1                       // zwracanie wartości
'''

W powyższym przypadku dla x > 1 wykona się podstawowa wersja funkcji, natomiast dla 
x == 1 nadpisujemy dwukrotnie funkcję fib. Ostatecznie fib(1) zwróci wartość 1 – wykona ostatnią ze zdefiniowanych wersji.

'''
func func_with_flows                            // definicja funkcji
{ 
    let xd { 123 }; 
    if( xd > 10 )
    {
        println(xd); 
    }                                           // blok operacji

    mut let mutable_var { 1 }; 
    while( mutable_var < 10 * xd ) 
    {
        mutable_var = mutable_var * xd;
    }

    for( mut let i = 0; i < 0; i = i + 1 )
    {
        mutable_var = mutable_var - xd;
    }
}
'''

Jak widać porównując powyższe przykłady każdy z bloków funkcji występujących po deklaracji można pominąć.

FUNKCJA MAIN
•	Funkcja podstawowa, która musi się znajdować w każdym pliku. Jej nazwa to main. Funkcja służy jako punkt wyjścia do wykonywania programy. Kontroluje wykonywanie programu przez kierowanie wywołań do innych funkcji.
•	Różnice między zwykłą funkcją a funkcją main - deklaracja
    o	Blok obowiązkowy 
        Słowo kluczowe oraz nazwa: func main
    o	Bloki opcjonalne 
        Występuje jedynie blok operacji
    o	Funkcji nie może mieć tylko jedną deklarację w kodzie
•	Przykład
'''
func main 
{
    let x { 10 }; 
    mut let y { 100 }; 

    println( fib(y) );

    // x = 12 - error bo const
    // y = 12 - ok bo mutable
} 
'''	









// komentarze



