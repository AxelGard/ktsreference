

# UShortArray

Creates a new array of the specified size, where each element is calculated by calling the specified init function.

```kotlin
@ExperimentalUnsignedTypesinline fun UShortArray(size: Int, init: (Int) -> UShort): UShortArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val ushorts = UShortArray(5) { i -> (i * 2).toUShort() }
    for (i in ushorts.indices) {
        println("ushorts[$i] = ${ushorts[i]}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-u-short-array.html)

    