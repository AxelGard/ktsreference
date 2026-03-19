

# toDoubleArray

Returns an array of Double containing all of the elements of this generic array.

```kotlin
fun Array<out Double>.toDoubleArray(): DoubleArray(source)
```

```kotlin
fun main() {
    val array = arrayOf(1.5, 2.5, 3.5)
    val doubleArray: DoubleArray = array.toDoubleArray()
    println(doubleArray.joinToString(prefix = "[", postfix = "]"))
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/to-double-array.html)

    