

# average

Returns an average value of elements in the array.

```kotlin
@JvmName(name = "averageOfByte")fun Array<out Byte>.average(): Double(source)
```

```kotlin
fun main() {
    val bytes = arrayOf<Byte>(10, 20, 30, 40)
    val avg = bytes.average()
    println("Average: $avg")
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/average.html)

    