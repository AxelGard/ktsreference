

# single

Returns the single element, or throws an exception if the array is empty or has more than one element.

```kotlin
fun <T> Array<out T>.single(): T(source)
```

```kotlin
fun main() {
    val singleElementArray = arrayOf("only one")
    val element = singleElementArray.single()
    println(element) // prints "only one"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/single.html)

    