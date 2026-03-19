

# maxBy

Returns the first character yielding the largest value of the given selector function.

```kotlin
@JvmName(name = "maxByOrThrow")inline fun <R : Comparable<R>> CharSequence.maxBy(selector: (Char) -> R): Char(source)
```

```kotlin
val text = "Hello, World!"
val maxChar = text.maxBy { it.code }   // selector returns Int (Comparable)
println(maxChar)   // prints 'w'
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-by.html)

    