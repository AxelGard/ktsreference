

# toUIntArray

Returns an array of UInt containing all of the elements of this generic array.

```kotlin
@ExperimentalUnsignedTypesfun Array<out UInt>.toUIntArray(): UIntArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val array: Array<UInt> = arrayOf(10u, 20u, 30u, 40u)
    val unsignedArray: UIntArray = array.toUIntArray()
    println(unsignedArray.joinToString())
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-u-int-array.html)

    