

# asShortArray

Returns an array of type ShortArray, which is a view of this array where each element is a signed reinterpretation of the corresponding element of this array.

```kotlin
@ExperimentalUnsignedTypesinline fun UShortArray.asShortArray(): ShortArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val uShorts: UShortArray = ushortArrayOf(0x0100u, 0xFF00u, 0x00FFu)
    val shorts: ShortArray = uShorts.asShortArray()
    println(shorts.joinToString(prefix = "[", postfix = "]"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/as-short-array.html)

    