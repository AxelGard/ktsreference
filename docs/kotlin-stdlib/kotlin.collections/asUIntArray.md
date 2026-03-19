

# asUIntArray

Returns an array of type UIntArray, which is a view of this array where each element is an unsigned reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun IntArray.asUIntArray(): UIntArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val intArray = intArrayOf(-1, 0, 1, 256, 65536)
    val uintArray: UIntArray = intArray.asUIntArray()
    println(uintArray.joinToString())          // prints: 4294967295, 0, 1, 256, 65536
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-u-int-array.html)

    