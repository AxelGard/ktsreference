

# toUByteArray

Returns an array of UByte containing all of the elements of this generic array.

```kotlin
@ExperimentalUnsignedTypesfun Array<out UByte>.toUByteArray(): UByteArray(source)
```

```kotlin
@OptIn(ExperimentalUnsignedTypes::class)
fun main() {
    val array: Array<UByte> = arrayOf(10.toUByte(), 20.toUByte(), 30.toUByte())
    val uByteArray: UByteArray = array.toUByteArray()
    println(uByteArray.joinToString(prefix = "[", postfix = "]"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-u-byte-array.html)

    