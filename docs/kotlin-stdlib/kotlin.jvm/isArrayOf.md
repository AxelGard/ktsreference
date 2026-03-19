

# isArrayOf

Checks if array can contain element of type T.

```kotlin
fun <T : Any> Array<*>.isArrayOf(): Boolean(source)
```

```kotlin
fun main() {
    val intArray: Array<Int> = arrayOf(1, 2, 3)
    println(intArray.isArrayOf<Int>())     // true
    println(intArray.isArrayOf<String>())  // false

    val anyArray: Array<Any> = arrayOf(1, "two", 3.0)
    println(anyArray.isArrayOf<Int>())     // true
    println(anyArray.isArrayOf<String>())  // true
    println(anyArray.isArrayOf<Double>())  // true
    println(anyArray.isArrayOf<Boolean>()) // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/is-array-of.html)

    