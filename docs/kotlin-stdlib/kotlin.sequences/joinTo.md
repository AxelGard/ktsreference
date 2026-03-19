

# joinTo

Appends the string from all the elements separated using separator and using the given prefix and postfix if supplied.

```kotlin
@IgnorableReturnValuefun <T, A : Appendable> Sequence<T>.joinTo(buffer: A, separator: CharSequence = ", ", prefix: CharSequence = "", postfix: CharSequence = "", limit: Int = -1, truncated: CharSequence = "...", transform: (T) -> CharSequence? = null): A(source)
```

```kotlin
val numbers = sequenceOf(1, 2, 3, 4, 5)

val sb = StringBuilder()
numbers.joinTo(
    buffer = sb,
    separator = " | ",
    prefix = "[",
    postfix = "]"
)

println(sb.toString())   // Output: [1 | 2 | 3 | 4 | 5]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.sequences/join-to.html)

    