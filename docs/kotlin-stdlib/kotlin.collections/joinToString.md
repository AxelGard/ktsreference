

# joinToString

Creates a string from all the elements separated using separator and using the given prefix and postfix if supplied.

```kotlin
fun <T> Array<out T>.joinToString(separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: (T) -> CharSequence? = null): String(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4, 5)

println(numbers.joinToString())                    // "1, 2, 3, 4, 5"
println(numbers.joinToString(separator = " | "))  // "1 | 2 | 3 | 4 | 5"
println(numbers.joinToString(prefix = "[", postfix = "]")) // "[1, 2, 3, 4, 5]"

println(numbers.joinToString(limit = 3, truncated = "...")) // "1, 2, 3..."
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/join-to-string.html)

    