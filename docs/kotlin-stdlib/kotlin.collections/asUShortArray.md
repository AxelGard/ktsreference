

# asUShortArray

Returns an array of type UShortArray, which is a view of this array where each element is an unsigned reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun ShortArray.asUShortArray(): UShortArray(source)
```

@ExperimentalUnsignedTypes
fun main() {
    val shorts = shortArrayOf(1000, -1, 32767, -32768)
    val ushorts: UShortArray = shorts.asUShortArray()
    println(ushorts.joinToString())  // prints: 1000, 65535, 32767, 32768
}

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-u-short-array.html)

    