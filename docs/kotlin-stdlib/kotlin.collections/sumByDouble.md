

# sumByDouble

Warning since 1.5

```kotlin
inline fun <T> Array<out T>.sumByDouble(selector: (T) -> Double): Double(source)
```

```kotlin
data class Item(val value: Double)

fun main() {
    val items = arrayOf(
        Item(10.5),
        Item(20.0),
        Item(30.25)
    )
    val total = items.sumByDouble { it.value }
    println("Total sum: $total")
}
```


[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/sum-by-double.html)

    