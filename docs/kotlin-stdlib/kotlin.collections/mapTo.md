

# mapTo

Applies the given transform function to each element of the original array and appends the results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R, C : MutableCollection<in R>> Array<out T>.mapTo(destination: C, transform: (T) -> R): C(source)
```

```kotlin
val numbers = arrayOf(1, 2, 3, 4)
val words = mutableListOf<String>()

numbers.mapTo(words) { "Number $it" }

println(words)  // [Number 1, Number 2, Number 3, Number 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-to.html)

    