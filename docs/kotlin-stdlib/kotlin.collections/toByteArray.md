

# toByteArray

Returns an array of Byte containing all of the elements of this generic array.

```kotlin
fun Array<out Byte>.toByteArray(): ByteArray(source)
```

```kotlin
fun main() {
    // Create an Array<Byte> containing the numbers 10, 20, 30, 40
    val byteArrayList: Array<Byte> = arrayOf(10, 20, 30, 40)

    // Convert the Array<Byte> to a ByteArray using toByteArray()
    val byteArray: ByteArray = byteArrayList.toByteArray()

    // Print the resulting ByteArray
    println(byteArray.joinToString(prefix = "[", postfix = "]"))  // Output: [10, 20, 30, 40]
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-byte-array.html)

    