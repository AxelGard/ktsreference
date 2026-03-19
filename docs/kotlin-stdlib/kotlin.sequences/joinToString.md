

# joinToString

Creates a string from all the elements separated using separator and using the given prefix and postfix if supplied.

```kotlin
fun <T> Sequence<T>.joinToString(separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: (T) -> CharSequence? = null): String(source)
```

```kotlin
val languages = sequenceOf("Kotlin", "Java", "Python")

val formatted = languages.joinToString(
    separator = " -> ",
    prefix = "<",
    postfix = ">",
    transform = { it.uppercase() }
)

println(formatted)   // Output: <KOTLIN -> JAVA -> PYTHON>
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/join-to-string.html)

    