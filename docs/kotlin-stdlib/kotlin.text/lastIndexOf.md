

# lastIndexOf

Returns the index within this char sequence of the last occurrence of the specified character, starting from the specified startIndex.

```kotlin
fun CharSequence.lastIndexOf(char: Char, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int(source)
```

```kotlin
val text = "Hello world, hello!"

// Find the last occurrence of 'l'
val lastL = text.lastIndexOf('l')
println(lastL) // 9

// Search backwards starting from index 5
val lastLFrom5 = text.lastIndexOf('l', startIndex = 5)
println(lastLFrom5) // 3

// Ignore case when searching for 'H'
val lastHIgnoreCase = text.lastIndexOf('H', ignoreCase = true)
println(lastHIgnoreCase) // 13
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/last-index-of.html)

    