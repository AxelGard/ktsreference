

# orEmpty

Returns this Collection if it's not null and the empty list otherwise.

```kotlin
inline fun <T> Collection<T>?.orEmpty(): Collection<T>(source)
```

```kotlin
val maybeNumbers: List<Int>? = null
val numbers = maybeNumbers.orEmpty()   // numbers is an empty List<Int> when maybeNumbers is null

println(numbers.isEmpty())            // true

// If maybeNumbers were not null, it would simply return the original collection
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/or-empty.html)

    