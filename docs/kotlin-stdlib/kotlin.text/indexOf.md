

# indexOf

Returns the index within this string of the first occurrence of the specified character, starting from the specified startIndex.

```kotlin
fun CharSequence.indexOf(char: Char, startIndex: Int = 0, ignoreCase: Boolean = false): Int(source)
```

```kotlin
val text = "Hello, World!"

val firstO = text.indexOf('o')          // 4
val secondO = text.indexOf('o', 5)      // 7
val ignoreCaseW = text.indexOf('w', 0, true) // 7

println("First 'o' at $firstO")
println("Second 'o' at $secondO")
println("Ignore case 'w' at $ignoreCaseW")
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/index-of.html)

    