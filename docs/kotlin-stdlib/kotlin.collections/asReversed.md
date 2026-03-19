

# asReversed

Returns a reversed read-only view of the original List. All changes made in the original list will be reflected in the reversed one.

```kotlin
fun <T> List<T>.asReversed(): List<T>(source)
```

```kotlin
val original = listOf(1, 2, 3, 4, 5)
val reversed = original.asReversed()

println("Original: $original")   // [1, 2, 3, 4, 5]
println("Reversed: $reversed")   // [5, 4, 3, 2, 1]

// Mutate the original list
val mutable = original.toMutableList()
mutable[0] = 99

println("After mutation:")
println("Original: $mutable")     // [99, 2, 3, 4, 5]
println("Reversed: ${mutable.asReversed()}") // [5, 4, 3, 2, 99]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-reversed.html)

    