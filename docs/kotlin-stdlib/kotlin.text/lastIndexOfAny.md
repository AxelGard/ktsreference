

# lastIndexOfAny

Finds the index of the last occurrence of any of the specified chars in this char sequence, starting from the specified startIndex and optionally ignoring the case.

```kotlin
fun CharSequence.lastIndexOfAny(chars: CharArray, startIndex: Int = lastIndex, ignoreCase: Boolean = false): Int(source)
```

```kotlin
val text = "Hello Kotlin, Kotlin is fun!"
val chars = charArrayOf('k', 'f')
val index = text.lastIndexOfAny(chars, ignoreCase = true)
println(index)   // prints the index of the last 'k' or 'f' in the string
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/last-index-of-any.html)

    