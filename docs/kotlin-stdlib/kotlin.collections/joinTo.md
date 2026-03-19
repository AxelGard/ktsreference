

# joinTo

Appends the string from all the elements separated using separator and using the given prefix and postfix if supplied.

```kotlin
@IgnorableReturnValuefun <T, A : Appendable> Array<out T>.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: (T) -> CharSequence? = null): A(source)
```

```kotlin
val numbers = arrayOf(10, 20, 30, 40, 50)
val sb = StringBuilder()
numbers.joinTo(
    buffer = sb,
    separator = ", ",
    prefix = "[",
    postfix = "]",
    limit = 3,
    truncated = "...",
    transform = { it.toString() }
)
println(sb.toString())   // prints: [10, 20, 30,...]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/join-to.html)

    