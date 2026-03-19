

# ULongArray

Creates a new array of the specified size, where each element is calculated by calling the specified init function.

```kotlin
@ExperimentalUnsignedTypesinline fun ULongArray(size: Int, init: (Int) -> ULong): ULongArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val uArray = ULongArray(5) { i -> (i.toULong() * i.toULong()) }
    println(uArray.joinToString(", "))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-long-array.html)

    