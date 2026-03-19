

# flatten

Returns a single list of all elements from all arrays in the given array.

```kotlin
fun <T> Array<out Array<out T>>.flatten(): List<T>(source)
```

```kotlin
val arrayOfArrays = arrayOf(
    arrayOf("a", "b"),
    arrayOf("c"),
    arrayOf("d", "e", "f")
)

val flatList: List<String> = arrayOfArrays.flatten()

println(flatList)  // [a, b, c, d, e, f]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/flatten.html)

    