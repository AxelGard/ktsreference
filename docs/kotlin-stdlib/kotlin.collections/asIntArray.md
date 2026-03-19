

# asIntArray

Returns an array of type IntArray, which is a view of this array where each element is a signed reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun UIntArray.asIntArray(): IntArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val unsigned = uintArrayOf(0u, 1u, 2u, 3u)
    val signed: IntArray = unsigned.asIntArray()

    println(signed.joinToString())   // prints: 0, 1, 2, 3
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-int-array.html)

    