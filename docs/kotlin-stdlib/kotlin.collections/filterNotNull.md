

# filterNotNull

Returns a list containing all elements that are not null.

```kotlin
fun <T : Any> Array<out T?>.filterNotNull(): List<T>(source)
```

```kotlin
val mixedArray: Array<String?> = arrayOf("apple", null, "banana", null, "cherry")
val nonNullList: List<String> = mixedArray.filterNotNull()

println(nonNullList) // Output: [apple, banana, cherry]
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/filter-not-null.html)

    