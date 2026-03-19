

# maxWith

Returns the first character having the largest value according to the provided comparator.

```kotlin
@JvmName(name = "maxWithOrThrow")fun CharSequence.maxWith(comparator: Comparator<in Char>): Char(source)
```

```kotlin
val text = "kotlin"
val maxChar = text.maxWith(Comparator<Char> { a, b -> a.compareTo(b) })
println("Maximum character: $maxChar")   // prints: t
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/max-with.html)

    