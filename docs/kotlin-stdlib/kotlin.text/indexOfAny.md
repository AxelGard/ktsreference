

# indexOfAny

Finds the index of the first occurrence of any of the specified chars in this char sequence, starting from the specified startIndex and optionally ignoring the case.

```kotlin
fun CharSequence.indexOfAny(chars: CharArray, startIndex: Int = 0, ignoreCase: Boolean = false): Int(source)
```

```kotlin
val text = "Hello, World!"
val delimiters = charArrayOf(',', '!')
val index = text.indexOfAny(delimiters)          // 5
val indexFrom7 = text.indexOfAny(delimiters, startIndex = 7) // 12
val indexIgnoreCase = "abcDEF".indexOfAny(charArrayOf('d'), ignoreCase = true) // 3
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/index-of-any.html)

    