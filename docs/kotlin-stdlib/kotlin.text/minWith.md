

# minWith

Returns the first character having the smallest value according to the provided comparator.

```kotlin
@JvmName(name = "minWithOrThrow")fun CharSequence.minWith(comparator: Comparator<in Char>): Char(source)
```

```kotlin
val text = "kotlin"
val smallest = text.minWith(Comparator { a, b -> a.compareTo(b) })
println("Smallest character: $smallest")  // Output: Smallest character: i
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/min-with.html)

    