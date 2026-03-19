

# indexOf

Returns first index of element, or -1 if the array does not contain element.

```kotlin
fun <T> Array<out T>.indexOf(element: T): Int(source)
```

```kotlin
fun main() {
    val fruits = arrayOf("apple", "banana", "cherry")

    val index = fruits.indexOf("banana")
    println(index)          // prints 1

    val missingIndex = fruits.indexOf("orange")
    println(missingIndex)   // prints -1
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/index-of.html)

    