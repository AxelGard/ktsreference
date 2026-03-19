

# getPolymorphicElement

Returns the current element if it is associated with the given key in a polymorphic manner or null otherwise. This method returns non-null value if either Element.key is equal to the given key or if the key is associated with Element.key via AbstractCoroutineContextKey. See AbstractCoroutineContextKey for the example of usage.

```kotlin
@ExperimentalStdlibApifun <E : CoroutineContext.Element> CoroutineContext.Element.getPolymorphicElement(key: CoroutineContext.Key<E>): E?(source)
```

```kotlin
import kotlin.coroutines.*

@ExperimentalStdlibApi
object MyKey : CoroutineContext.Key<MyElement>, AbstractCoroutineContextKey<MyElement, MyOtherKey>

object MyOtherKey : CoroutineContext.Key<MyElement>

data class MyElement(val text: String) : AbstractCoroutineContextElement(MyKey)

fun main() {
    // Create a context that contains our element
    val ctx: CoroutineContext = MyElement("Hello, Kotlin!")

    // Retrieve the element directly by its own key
    val element = ctx[MyKey]!!
    val sameKey = element.getPolymorphicElement(MyKey)
    println("Same key -> ${sameKey?.text}")   // prints: Hello, Kotlin!

    // Retrieve the element using a polymorphic key
    val polyKey = element.getPolymorphicElement(MyOtherKey)
    println("Polymorphic key -> ${polyKey?.text}")   // prints: Hello, Kotlin!
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.coroutines/get-polymorphic-element.html)

    