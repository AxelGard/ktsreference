

# mapNotNullTo

Applies the given transform function to each element in the original array and appends only the non-null results to the given destination.

```kotlin
@IgnorableReturnValueinline fun <T, R : Any, C : MutableCollection<in R>> Array<out T>.mapNotNullTo(destination: C, transform: (T) -> R?): C(source)
```

```kotlin
val numbers: Array<Int?> = arrayOf(1, null, 3, 4, null)

val nonNullNumbers = mutableListOf<Int>()
numbers.mapNotNullTo(nonNullNumbers) { it }   // identity transform

println(nonNullNumbers)   // prints: [1, 3, 4]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/map-not-null-to.html)

    