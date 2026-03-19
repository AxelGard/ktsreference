

# sort

Sorts the array in-place.

```kotlin
@ExperimentalUnsignedTypesfun UIntArray.sort()(source)
```

@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val numbers = uintArrayOf(5u, 3u, 9u, 1u)
    numbers.sort()
    println(numbers.joinToString())  // Output: 1, 3, 5, 9
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sort.html)

    