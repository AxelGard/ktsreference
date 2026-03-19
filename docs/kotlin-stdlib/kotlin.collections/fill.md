

# fill

Fills this array or its subrange with the specified element value.

```kotlin
@ExperimentalUnsignedTypesfun UIntArray.fill(element: UInt, fromIndex: Int = 0, toIndex: Int = size)(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    // Create an array of 5 unsigned integers
    val numbers = UIntArray(5)

    // Fill the whole array with 42u
    numbers.fill(42u)
    println(numbers.joinToString())  // 42, 42, 42, 42, 42

    // Fill a subrange (indices 1..3) with 99u
    numbers.fill(99u, fromIndex = 1, toIndex = 4)
    println(numbers.joinToString())  // 42, 99, 99, 99, 42
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/fill.html)

    